"""
Question:

The Builder pattern constructs objects step-by-step. One common example is building SQL queries dynamically. Can you implement a query builder in Python that supports “SELECT”, “WHERE”, and “LIMIT” clauses?

Answer:

The Builder pattern can be implemented by creating a class that builds the SQL query incrementally. Each method modifies the query and returns the builder instance, allowing for method chaining.
Clause ordering is enforced (i.e., the SELECT clause must be defined before WHERE and LIMIT) through conditions at build time. This ensures that the generated SQL query is syntactically correct.
"""

class QueryBuilder:
    def __init__(self):
        self._select = None
        self._where = None
        self._limit = None

    def select(self, columns):
        self._select = f"SELECT {columns}"
        return self

    def where(self, condition):
        self._where = f"WHERE {condition}"
        return self

    def limit(self, count):
        self._limit = f"LIMIT {count}"
        return self

    def build(self):
        if not self._select:
            raise ValueError("A SELECT clause is required.")
        query = self._select
        if self._where:
            query += f" {self._where}"
        if self._limit:
            query += f" {self._limit}"
        return query

query = QueryBuilder()
query = query.select("*").where("age > 18").limit(10).build()
print(query)  # SELECT * WHERE age > 18 LIMIT 10
