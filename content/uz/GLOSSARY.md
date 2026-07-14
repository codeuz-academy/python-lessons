---
title: Uzbek Translation Glossary
description: Internal glossary for Uzbek content terminology
permalink: false
eleventyExcludeFromCollections: true
---

# Uzbek Translation Glossary

Ushbu glossariy `content/uz` bo'limidagi darslar uchun yagona terminologiya qoidasini belgilaydi.

## Asosiy qoidalar

- Tarjima tabiiy va ravon o'zbek tilida bo'lishi kerak.
- Agar atama uchun tabiiy o'zbekcha muqobil yo'q bo'lsa, inglizcha variant saqlanadi.
- Texnik atama birinchi marta uchraganda o'zbekcha + inglizcha ko'rinishdan foydalaning: `qamrov (scope)`, `kesim (slice)`.
- Keyingi o'rinlarda bir xil shaklni izchil qo'llang.
- Ko'plik qo'shimchasi: inglizcha atama + `'lar` — `exception'lar`, `iterator'lar`, `decorator'lar`.

---

## Ma'lumot turlari

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| string | satr / matn (`string`) | Matnda satr yoki matn, kodda `str` |
| integer | butun son (`integer`) | Kodda `int` |
| float | o'nlik kasr son (`float`) | Kodda `float` |
| boolean | mantiqiy qiymat (`boolean`) | Kodda `bool` |
| complex | kompleks son (`complex`) | `xayoliy` qism uchun — mavhum emas |
| list | ro'yxat (`list`) | Matnda ro'yxat, kodda `list` |
| tuple | `tuple` | `kortej` ishlatilmaydi |
| dictionary | lug'at (`dictionary`) | Matnda lug'at, kodda `dict` |
| set | to'plam (`set`) | Matnda to'plam |
| frozenset | `frozenset` | O'zgarmas to'plam |
| NoneType | `None` | O'zgartirilmaydi |

## Asosiy tushunchalar

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| variable | o'zgaruvchi (`variable`) | |
| function | funksiya | |
| parameter | parametr | |
| argument | argument | |
| return | `return` | Kalit so'z sifatida |
| expression | ifoda (`expression`) | |
| statement | buyruq (`statement`) | |
| loop | takrorlash (`loop`) | |
| condition | shart | |
| comment | izoh (`comment`) | |
| docstring | `docstring` | O'zgartirilmaydi |
| indentation | indentatsiya | Qator boshidagi bo'sh joy |
| data type | ma'lumot turi (`data type`) | |
| literal | literal | |
| index | indeks | |
| slice | kesim (`slice`) | |
| slicing | kesim olish (`slicing`) | |
| key-value | kalit-qiymat (`key-value`) | Lug'at kontekstida |
| method | metod | |
| object | obyekt | |
| sequence | ketma-ketlik (`sequence`) | |
| iteration | iteratsiya | |
| iterable | `iterable` | O'zgartirilmaydi |
| membership | a'zolik (`membership`) | `in/not in` kontekstida |
| scope | qamrov (`scope`) | Birinchi uchrashda izoh bilan |
| namespace | nomlar makoni (`namespace`) | Modul/import kontekstida |
| built-in | o'rnatilgan (`built-in`) | Funksiya/modul/metodlar uchun |
| immutable | o'zgarmas (`immutable`) | |
| mutable | o'zgaruvchan (`mutable`) | |
| hashable | `hashable` | O'zgartirilmaydi |
| shallow copy | yuzaki nusxa (`shallow copy`) | Lug'at/list nusxalashda |
| concatenation | birlashtirish (`concatenation`) | |
| lambda | `lambda` | O'zgartirilmaydi |
| anonymous function | anonim funksiya | Lambda kontekstida |
| case-sensitive | katta-kichik harflarni farqlaydi | |
| escape sequence | `escape sequence` | O'zgartirilmaydi |
| f-string | `f-string` | O'zgartirilmaydi |
| raw string | `raw string` | O'zgartirilmaydi |
| list comprehension | `list comprehension` | O'zgartirilmaydi |
| generator expression | generator ifodasi | |
| lazy evaluation | `lazy evaluation` | O'zgartirilmaydi |
| ternary operator | bir qatorli shart | |

## OOP tushunchalari

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| class | sinf (`class`) | |
| object / instance | obyekt / `instance` | |
| attribute | atribut | |
| class attribute | klass atributi | |
| instance attribute | obyekt atributi | |
| inheritance | meros olish (`inheritance`) | |
| encapsulation | `Encapsulation` | |
| polymorphism | `Polymorphism` | |
| operator overloading | `Operator overloading` | |
| constructor | konstruktor | `__init__` metodi |
| dunder | `dunder` | Double underscore metodlari |
| blueprint | shablon | Sinf tushuntirish kontekstida |
| decorator | dekorator (`decorator`) | |
| closure | `Closure` | |
| wrapper | o'rovchi (`wrapper`) | |
| @dataclass | `@dataclass` | O'zgartirilmaydi |

## Modullar va paketlar

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| module | modul | |
| package | paket | |
| import | `import` | Kalit so'z sifatida |
| standard library | standart kutubxona | |
| third-party | uchinchi tomon | |
| virtual environment | virtual muhit | |
| pip | `pip` | O'zgartirilmaydi |
| package manager | paket menejeri | |
| dependency | bog'liqlik | |
| version | versiya | |
| upgrade | yangilash | |
| freeze | `freeze` | `pip freeze` kontekstida |
| working directory | ishchi papka | |
| circular import | aylanma import | |
| site-packages | `site-packages` | O'zgartirilmaydi |

## Xatolar va istisnolar

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| exception | `exception` | Ko'plikda `exception'lar` |
| try / except / finally | `try` / `except` / `finally` | Kalit so'zlar |
| raise | `raise` | |
| handler | `handler` | Majburan tarjima qilinmaydi |
| re-raise | qayta ko'tarish | |
| custom exception | maxsus `exception` | |
| assertion | `assert` | |
| sanity check | mantiqiy tekshiruv (`sanity check`) | Assertion kontekstida |

## Fayl va I/O

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| input / output (I/O) | kirish / chiqish (`I/O`) | |
| standard output | `standard output` | |
| mode | rejim / `mode` | Fayl ochish kontekstida |
| append | qo'shib yozish | |
| overwrite | ustiga yozish | |
| binary mode | `binary mode` | |
| with | `with` | Kalit so'z sifatida |

## Ma'lumotlar bazasi

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| database | ma'lumotlar bazasi | |
| connection | ulanish | |
| cursor | `cursor` | |
| query | so'rov (`query`) | |
| commit | `commit` | |
| rollback | `rollback` | |
| fetch | olish (`fetch`) | |
| credentials | kirish ma'lumotlari | |
| parameterized query | `parameterized query` | |
| SQL injection | `SQL injection` | |
| context manager | kontekst menejer (`context manager`) | |
| adapter | adapter | |

## Tarmoq va veb

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| networking | tarmoq | |
| socket | `socket` | |
| client | mijoz | |
| server | `server` | |
| endpoint | `endpoint` | "Tugun" majburiy ishlatilmaydi |
| TCP / UDP | `TCP` / `UDP` | O'zgartirilmaydi |
| timeout | `timeout` | |
| web development | veb dasturlash | |
| framework | freymvork | |
| microframework | mikrofreymvork | |
| API | `API` | O'zgartirilmaydi |
| RESTful | `RESTful` | |
| deploy | joylashtirish (`deploy`) | |
| scalability | masshtablilik | |
| templating | shablonlar | |
| cookie | `cookie` | |

## Ilg'or (Advanced) tushunchalar

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| type hint | `type hint` | |
| annotation | `annotation` | |
| TypedDict | `TypedDict` | |
| iterator | `iterator` | Ko'plikda `iterator'lar` |
| generator | `generator` | Ko'plikda `generator'lar` |
| yield | `yield` | Kalit so'z sifatida |
| StopIteration | `StopIteration` | Exception nomi |
| context manager | kontekst menejer (`context manager`) | |
| metaclass | `metaclass` | |
| metaprogramming | metadasturlash | |
| thread | `thread` | |
| process | `process` | |
| multithreading | `multithreading` | |
| multiprocessing | `multiprocessing` | |
| concurrency | bir vaqtlilik (`concurrency`) | |
| parallelism | `parallelism` | |
| GIL | `GIL` | Global Interpreter Lock |
| I/O Bound | `I/O Bound` | |
| CPU Bound | `CPU Bound` | |
| overhead | `overhead` | |
| async / await | `async` / `await` | Kalit so'zlar |
| coroutine | `coroutine` | |
| design pattern | `design pattern` | |
| Singleton | `Singleton` | |
| Factory | `Factory` | |
| Observer | `Observer` | |
| Strategy | `Strategy` | |
| subscriber | obunachi (`subscriber`) | Pub/Sub kontekstida |
| plugin | plagin (`plugin`) | |
| serialization | serializatsiya | |
| unit test | `unit test` | |
| mock / mocking | `mock` / `mocking` | |
| coverage | qamrov (`coverage`) | Kod qamrovi |
| TDD | `TDD` | Test Driven Development |
| memory management | xotira boshqaruvi | |
| garbage collection | `Garbage collection` | |
| reference counting | `reference counting` | |
| stack memory | `Stack memory` | |
| heap memory | `Heap memory` | |
| circular reference | `circular reference` | |
| memory-efficient | xotira tejamkor | |

## Umumiy texnik atamalar

| English | Tavsiya etilgan yozuv | Izoh |
| --- | --- | --- |
| runtime | bajarilish vaqti (`runtime`) | "Dastur bajarilishi vaqtida" kabi |
| development | ishlab chiqish (`development`) | |
| debug | nosozliklarni topish (`debug`) | "debug qilish" o'rniga |
| performance | unumdorlik (`performance`) | |
| refactoring | refaktoring (`refactoring`) | Yoki "kodni qayta tuzish" |
| maintainable | qo'llab-quvvatlash oson | |
| over-engineering | ortiqcha murakkablashtirish | |
| reusable | qayta ishlatiladigan | |
| interpreter | `interpreter` | |
| compile | kompilyatsiya | |
| dynamic typing | dinamik til | |
| JSON | `JSON` | O'zgartirilmaydi |
| parse | `parse` | |
| regex | `RegEx` | Regular Expression |
| pattern | `pattern` | RegEx kontekstida |
| metadata | meta-ma'lumotlar | |
| version control | `version control` | |
| shell | terminal qobig'i | |

---

## Qochish kerak bo'lgan variantlar

- `kortej` → `tuple`
- `Birinci` → `Birinchi`
- `mavhum` (complex son kontekstida) → `xayoliy`
- `behavior'ni`, `behavior'ini` → `xatti-harakatni` yoki `behaviorni`
- `debug qilish` → `nosozliklarni topish`
