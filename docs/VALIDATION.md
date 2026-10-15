# Проверка первого этапа — 15 октября 2026

## Выполнено

- Клонирован Amethyst-iOS, commit `f98c4133c72d39e06ceac42b57cc4477c52105fc`.
- Загружены все рекурсивные git submodules. Для checkout на Windows использован
  `git -c core.longpaths=true submodule update --init --recursive`.
- Изучены README, GPL v3 LICENSE, Makefile, CMakeLists.txt, JavaApp/Makefile,
  workflows, sideload entitlements, локальная авторизация и интеграция JIT.
- Создан отдельный workflow для GitHub hosted macOS runner. Интерфейс и Makefile не изменены.
  В JavaLauncher.m добавлен mach/mach.h для объявления используемых функций Mach.
- Синтаксис YAML разобран PyYAML 6.0.3; проверены наличие macOS runner и ручного trigger.
- Все блоки `run` прошли синтаксическую проверку `sh -n` из Git for Windows.
- Python-код проверки IPA прошёл `ast.parse`.
- `git diff --check --ignore-submodules=all` прошёл.
- HEAD-запросы к upstream ZIP runtimes Java 8/17/21/25 вернули HTTP 200.
  Это проверка доступности URL, а не проверка содержимого runtime.

## Подтверждённая сборка GitHub Actions

Успешный run: https://github.com/YRSL64/Amethyst-iOS/actions/runs/38724578743
Commit: `cebebe0fa3f00dda7323aaf4999d57553dcf5082`.

- macOS 15 ARM64, Xcode 26.3, iPhoneOS SDK 26.2, Zulu JDK 8.
- Компиляция нативных компонентов и Java-кода завершилась успешно.
- Штатный Makefile сформировал `org.angelauramc.amethyst-1.0-ios.ipa`.
- Проверены CRC ZIP, Info.plist, Mach-O, launcher.jar/lwjgl.jar и runtimes 8/17/21/25.
- IPA artifact: https://github.com/YRSL64/Amethyst-iOS/actions/runs/38724578743/artifacts/11968070731
- Diagnostics: https://github.com/YRSL64/Amethyst-iOS/actions/runs/38724578743/artifacts/11967940711
- Размер artifact ZIP: 189343069 байт.
- SHA256 artifact ZIP: `da9f172673f77bcfee942030fcb57939f257603e972877119cd268c22c73e15b`.

В ходе CI исправлены: отсутствие Temurin JDK 8 для ARM64 macOS (выбран Zulu),
отсутствующий include mach/mach.h и выбор устаревшего Xcode по умолчанию.

## Не выполнено

- Проверка установки, Apple provisioning, доступных entitlements и Microsoft OAuth.
- JIT на iOS 27, запуск Java 21 и Minecraft 1.21.4 на iPhone 17 Pro Max.
- Работа рендереров, миров, серверов, Fabric, модов, производительность и нагрев.

## Технические наблюдения

- Реальная сборка идёт через Makefile/CMake, поэтому workflow не ограничен
  вызовом xcodebuild над существующим .xcodeproj.
- Build JDK — версия 8, игровые iOS runtimes поставляются отдельно.
- Штатный package target уже формирует IPA с Payload; ldid не выдаёт Apple подпись.
- Makefile удаляет legal/LICENSE из рабочих runtimes; новый workflow предварительно
  сохраняет их в resources/runtime-licenses, чтобы они попали в Payload.
- Репозиторий содержит готовые нативные библиотеки. Их пересборка и полная проверка
  происхождения в этой сессии не выполнялись.
- Поддержка iOS 26 в исходном коде не считается доказательством поддержки iOS 27.

## Следующее необходимое действие

Скачать artifact, извлечь IPA, подписать и установить его с Windows по README.ru.md.
Затем проверить открытие приложения, доступность JIT и запуск игры на телефоне.
Брендинг и дизайн в этом PR не менялись.
