#inside virtualenv
source venv/bin/activate
#execute following scripts
jar2tmp and 
jarscan.py
# Results
pom file results stored in a flat file.

Example of projects in a package #4
+- org.antlr:antlr:jar:3.4:compile
|  +- org.antlr:antlr-runtime:jar:3.4:compile
|  |  +- org.antlr:stringtemplate:jar:3.2.1:compile
|  |  \- antlr:antlr:jar:2.7.7:compile
|  \- org.antlr:ST4:jar:4.0.4:compile
