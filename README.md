# README


## API End Points

|Resource| Verb  | Request URI             |Request Headers|Request Body   | Action           |
|--------|--------|------------------------|---------------|---------------|------------------|
|Profile | POST   | `/login`               |      Empty    |data           | `signup`         |
|        | POST   | `/profile`             |      Empty    |data           | `signin`         |
|        | GET    | `/profile/:id`         |      Token    |Empty          | `profile data`   |
|        | DELETE | `/profile/:id`         |      Token    |Empty          | `delete profile` |
|        | PATCH  | `/profile/:id`         |      Token    |data           | `changepw`       |
|Expenses| GET    | `/expenses`            |      Token    |Empty          | `Expenses Index` |
|        | POST   | `/expenses`            |      Token    |data           | `Add Expense`    |
|        | PATCH  | `/expenses/:id`        |      Token    |data           | `Update Expense` |
|        | DELETE | `/expenses/:id`        |      Token    |Empty          | `Delete Expense` |
|Incomes | GET    | `/incomes`             |      Token    |Empty          | `Incomes Index`  |
|        | POST   | `/incomes`             |      Token    |data           | `Add Income`     |
|        | PATCH  | `/incomes/:id`         |      Token    |data           | `Update Income`  |
|        | DELETE | `/incomes/:id`         |      Token    |Empty          | `Delete Income`  |
|Budget  | GET    | `/budget`              |      Token    |Empty          | `Budgets Index`  |
|        | POST   | `/budget`              |      Token    |data           | `Add Budget`     |
|        | PATCH  | `/budget/:id`          |      Token    |data           | `Update Budget`  |
|        | DELETE | `/budget/:id`          |      Token    |Empty          | `Delete Budget`  |