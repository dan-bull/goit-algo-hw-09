**Порівняння ефективності**

-   **Час виконання (O-велике):**

    -   **Жадібний алгоритм:** O(n), де n - кількість номіналів монет. Він дуже швидкий, оскільки просто перебирає монети у порядку спадання.
    -   **Динамічне програмування:** O(n * amount). Хоча він складніший, його час виконання все ще досить прийнятний для більшості практичних завдань.
-   **Продуктивність при великих сумах:**

    -   **Жадібний алгоритм:** Добре працює з великими сумами, оскільки його складність не залежить від суми.
    -   **Динамічне програмування:** Також добре працює з великими сумами, хоча його час виконання може зростати лінійно зі збільшенням суми.
-   **Оптимальність:**

    -   **Жадібний алгоритм:** Не завжди знаходить оптимальне рішення. Наприклад, для номіналів монет [1, 3, 4] та суми 6, він видасть [4, 1, 1], хоча оптимальне рішення - [3, 3].
    -   **Динамічне програмування:** Завжди знаходить оптимальне рішення, оскільки розглядає всі можливі комбінації монет.

**Висновки**

Обидва алгоритми ефективні для знаходження монет для заданої суми. Жадібний алгоритм простіший і швидший, але не завжди знаходить оптимальне рішення. Динамічне програмування гарантує оптимальність, але може бути трохи повільнішим при дуже великих сумах. Вибір алгоритму залежить від конкретних вимог до точності та швидкодії.