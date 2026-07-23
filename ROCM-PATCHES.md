# Патчи для сборки ROCm на Chimera Linux

Заметка о том, какие патчи понадобились для сборки ROCm-стека и почему.
Основные причины делятся на три группы:

1. **musl вместо glibc** — отсутствуют glibc-расширения (`dladdr1`,
   транзитивные заголовки, `basename` в другом хедере, поведение `dlerror`).
2. **libc++ / compiler-rt / libunwind вместо libstdc++ / libgcc** — строже
   следование стандарту C++, нет `libstdc++fs`, нет `libgcc_s`.
3. **LLVM/clang 22 (системный) вместо ванильного ROCm LLVM** — более строгая
   проверка типов и переименованные/удалённые API компилятора.

Плюс отдельные мелочи под cmake 4.x и парсер заголовков в roctracer.

---

## rocm-device-libs

**`llvm-22-compat.patch`** — LLVM 22.
Clang 22 требует явного target-feature `cube-insts` для `__builtin_amdgcn_lerp`.
Добавлен атрибут `target("cube-insts")` (`CRATTR`) на cubemap-варианты
`image_load`/`image_store`. Иначе сборка device-libs падает с
`'__builtin_amdgcn_lerp' needs target feature cube-insts`.
Бэкпорт из upstream `amd-staging`.

## rocm-comgr

**`6.4.1-extend-isa-compatibility-check.patch`** — совместимость ISA.
Позволяет грузить кернелы по совместимости ISA (например, кернел gfx1030
запускать на gfx1036). Основано на патче Debian от Cordell Bloor. Нужно,
чтобы собранные под один gfx-таргет ядра работали на близких GPU.

**`7.2.0-llvm-22-compat.patch`** — LLVM 22.
Переименованные API clang: `setFileManager(new FileManager(...))` →
`setVirtualFileSystem(&FS)`, и флаг `-Xclang -no-disable-free` →
`-disable-free=false`. Частичный бэкпорт upstream-коммита.

## roct-thunk-interface (libhsakmt)

**`functions.patch`** — экспорт символов.
Добавляет недостающие символы в version-script `libhsakmt.ver`
(`hsaKmtCreateQueueExt`, `hsaKmtRegisterGraphicsHandleToNodesExt`,
`hsaKmtModelEnabled`). Линкер в Chimera строгий к version-script: если символ
используется, но не перечислен — ошибка. См. ROCm/rocm-systems#284.

## rocr-runtime (HSA runtime)

**`use-system-hsakmt.patch`** — системный libhsakmt.
Вводит опцию `BUILD_HSAKMT`: вместо сборки vendored-копии libhsakmt берётся
системный через `find_package(hsakmt)` (пакет roct-thunk-interface). Убирает
дублирование.

**`fix-libcxx.patch`** — libc++.
libc++ строже: `std::map<hsa_signal_t, ...>` не компилируется без явного
компаратора (libstdc++ пропускал сравнение структур через `std::less<void>`).
Добавлен явный компаратор `HsaSignalLess`. См. ROCm/rocm-systems#3307.

**`llvm-22-compat.patch`** — LLVM 22 (строгая проверка типов).
`bool`-функция не может возвращать `NULL` → `false`; `uint64_t`-функция
не может возвращать `NULL` → `0`.

## rocprofiler-register

**`no-cpack.patch`** — cmake 4.x + libc++.
`cpack_add_component_group` требует явного `include(CPackComponent)` (в cmake
4.x уже не подключается неявно) — cpack-пакеты мы не собираем, просто убрано.
Плюс системные `fmt`/`glog` сделаны глобальными imported-таргетами, и убран
fallback `-lstdc++fs` (в libc++ filesystem встроен).

## roctracer

**`preprocess-no-linemarkers.patch`** — парсер заголовков.
Форк CppHeaderParser (robotpy) давится на linemarker'ах препроцессора внутри
тел enum'ов. Добавлен флаг `-P` в вызовы `${CMAKE_C_COMPILER} -E`, чтобы
`.i`-файлы шли без linemarker'ов (они всё равно парсятся только ради сигнатур).

**`gen-ostream-multi-typedef.patch`** — парсер заголовков.
CppHeaderParser не умеет `typedef enum {...} A, B;` (несколько имён, как в
HIP-хедерах) — второе имя выносится в отдельный typedef перед парсингом. Также
обработаны анонимные struct/union, которые форк называет `<anon-struct-N>`.

**`no-tests.patch`** — тесты + `-Werror`.
Тесты используют устаревший модуль FindHIP и требуют железа amdgpu — отключены.
Заодно убран `-Werror`.

## rocblas

**`musl-libcxx-link.patch`** — libc++ / линковка.
На Chimera (libc++ + compiler-rt) C++17 filesystem живёт в самом libc++, так
что `-lstdc++fs` не существует; unwinding даёт libunwind, не libgcc. Заменено
`-lstdc++fs --unwindlib=libgcc` → `--unwindlib=libunwind`.

**`musl-sys-types.patch`** — musl.
`rocblas_ostream.hpp` использует `dev_t`/`ino_t`, которые на glibc приходят
транзитивно, а musl требует явного `#include <sys/types.h>`.

## rocsolver

**`musl-libcxx-link.patch`** — libc++ / линковка.
То же, что у rocblas: захардкоженный `--unwindlib=libgcc` ломает линковку
`librocsolver.so` (`unable to find library -lgcc_s`). Заменён на
`--unwindlib=libunwind`.

## rocfft

**`musl-library-path.patch`** — musl.
У musl нет `dladdr1()`/`RTLD_DL_LINKMAP` (glibc-расширения). Обычный `dladdr()`
уже кладёт путь к .so в `Dl_info::dli_fname` — ровно то, что rocFFT нужно,
чтобы найти кэш кернелов рядом с `librocfft.so`. Используем его.

## miopen

**`boost-optional-explicit-ctor.patch`** — новый Boost.
Конвертирующий конструктор `boost::optional` теперь `explicit`, поэтому
copy-list-initialization `return {x};` больше не компилируется. Возвращаем
значение напрямую (`return x;`). `std::optional` не затронут.

---

## Правки не через .patch (inline в template.py)

### hip (`post_patch`)

- **musl:** `basename` объявлен только в `<libgen.h>` — добавлен `#include`
  в `rocclr/os/os_posix.cpp`.
- **libc++ `<ranges>`:** макрос `#define __local __attribute__((...))`
  затирает приватный идентификатор, который libc++ использует в `<ranges>`
  (`join_view`), ломая любой HIP-TU, тянущий C++20-ranges (например,
  nlohmann/json). Макрос убран, атрибут заинлайнен прямо в функцию
  `__to_local`.
- **LDFLAGS:** `-Wl,--undefined-version` — version-script перечисляет hiprtc-
  символы, живущие в отдельной `libhiprtc`.

### btop (`patches/rsmi-clear-stale-dlerror.patch`)

Не часть ROCm, но связано: musl держит ошибку `dlerror()` до её чтения,
поэтому после неудачных `dlopen`-кандидатов проверка символов в `rsmi_init`
ложно падает и AMD-мониторинг не инициализируется. Добавлен пустой вызов
`dlerror()` для сброса устаревшей ошибки.
