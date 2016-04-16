mvn -q dependency:copy-dependencies -DoutputDirectory=myfolder1
mvn dependency:tree -DoutputFile=graphml -DoutputType='tgf'
