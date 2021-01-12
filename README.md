# PLATUML - JAVA

converts palantuml's uml class diagram markdown to java class

### demo

---
### input : text.pu
```
@startuml

class Bank {
- accounts : Account[]
+ manages() : void
}

class Account{
- number : int
- balance : double
+ deposite(amount : double) : boolean
+ withdraw(double) : boolean
}

class Saving_Account {
- account_number : int
+ get_interest() : void
}

Bank *-- Account
Account <|-- Saving_Account

@enduml
```

### Plant uml rendering

![plant uml rendering](https://imgur.com/6XwYU0k.png)
---

### output

#### **Account.java**
```java
public class Account
{
	private int number;

	private double balance;

	public boolean deposite (double amount){};

	public boolean withdraw (){};

}
```
#### **Saving_Account.java**
```java
public class Saving_Account extends Account
{
	private int account_number;

	public void get_interest (){};

}
```
#### **Bank.java**
```java
public class Bank
{
	private Account[] accounts;

	public void manages (){};

}
```

# RUN
edit text.pu to input uml markdown

type the following commands in terminal

`make clean` or `rm *db ` `rm *.java`

`make run` or `py Driver.py`


the output file will be same name as the class name with an extension of java
