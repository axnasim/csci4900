mvn -f pom.xml dependency:copy-dependencies  -DoutputDirectory=dpdncy
mvn -f pom.xml dependency:tree -Doutput=file.graphml 
