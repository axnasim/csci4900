mvn -f pom.xml dependency:copy-dependencies  -DoutputDirectory=dpdncy
mvn -f pom.xml dependency:tree -Doutput=tgf -Doutput=dependency.txt
grep -a1 "|  +- " dependency.txt > dplevels.txt
