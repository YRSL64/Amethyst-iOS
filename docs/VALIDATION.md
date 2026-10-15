# Проверка первого этапа — 15 октября 2026

## Выполнено

- Клонирован Amethyst-iOS, commit `f98c4133c72d39e06ceac42b57cc4477c52105fc`.
- Загружены все рекурсивные git submodules. Для checkout на Windows использован
  `git -c core.longpaths=true submodule update --init --recursive`.
- Изучены README, GPL v3 LICENSE, Makefile, CMakeLists.txt, JavaApp/Makefile,
  workflows, sideload entitlements, локальная авторизация и интеграция JIT.
- Создан отдельный workflow для GitHub hosted macOS runner. Штатные исходники
  приложения, Makefile и ресурсы интерфейса не изменены.
- Синтаксис YAML разобран PyYAML 6.0.3; проверены наличие macOS runner и ручного trigger.
- Все блоки `run` прошли синтаксическую проверку `sh -n` из Git for Windows.
- Python-код проверки IPA прошёл `ast.parse`.
- `git diff --check --ignore-submodules=all` прошёл.
- HEAD-запросы к upstream ZIP runtimes Java 8/17/21/25 вернули HTTP 200.
  Это проверка доступности URL, а не проверка содержимого runtime.

## Не выполнено

- Компиляция Objective-C/C++/Java: локально Xcode и macOS отсутствуют; результат macOS CI фиксируется отдельно.
- Результаты Actions: см. актуальный запуск в PR ветки yrsl-launcher.
- Создание/проверка настоящего IPA: файла нет. Проверяющий скрипт будет выполнен
  на реальном результате в CI. Его синтаксическая проверка не подтверждает упаковку.
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

Доступ к YRSL64/Amethyst-iOS подтверждён, ветка yrsl-launcher создана.
Workflow опубликован. Необходимо дождаться результата macOS CI и проверить логи.
После успешной baseline-сборки можно переходить к изменениям приложения.
