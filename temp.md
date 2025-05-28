flowchart TD
    A[Start: Addition Problem] --> B[Identify First Number]
    B --> C[Identify Second Number] 
    C --> D[Combine the Numbers]
    D --> E[Calculate Sum]
    E --> F[Result: Final Answer]
    
    A ~~~ A1{{The process begins when we encounter numbers that need to be combined}}
    B ~~~ B1{{Also called the first addend - Example: In 5 + 3 the first number is 5}}
    C ~~~ C1{{Also called the second addend - Example: In 5 + 3 the second number is 3}}
    D ~~~ D1{{Addition means putting quantities together using counting or mental math}}
    E ~~~ E1{{The sum is the total when addends are combined - Example: 5 + 3 = 8}}
    F ~~~ F1{{The final answer represents the total quantity - Check if result makes sense}}
    
    classDef mainBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef resultBox fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef annotation fill:#fffde7,stroke:#f57f17,stroke-width:1px,stroke-dasharray: 3 3
    
    class A,B,C,D,E mainBox
    class F resultBox
    class A1,B1,C1,D1,E1,F1 annotation
