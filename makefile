all:
	py Driver.py
	cat *.java
run:	
	py Driver.py
	cat *.java
clean: 
	rm *.db
	rm *.java