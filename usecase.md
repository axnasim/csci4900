## Title - Use Case

## Primary Actor
Developers, End Users

## Goal in context
Use pom.xml file to get the relationships and post the results in SPDX DB.

maven-dependency-plugin

<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>${junit.version}</version>
</dependency></ul>

<dependency><groupId>org.springframework</groupId>
<artifactId>spring-core</artifactId>
<version>4.2.4.RELEASE</version>
</dependency>

## License Information

LicenseID: LicenseRef-Apache-possibility
LicenseName: Apache-possibility
ExtractedText: <text></text>
LicenseCrossReference: 
LicenseComment: <text>found by nomos</text>

LicenseID: LicenseRef-GPL
LicenseName: GPL
ExtractedText: <text></text>
LicenseCrossReference: 
LicenseComment: <text>found by nomos</text>

LicenseID: LicenseRef-MIT-style
LicenseName: MIT-style
ExtractedText: <text></text>
LicenseCrossReference: 
LicenseComment: <text>found by nomos</text>

## Stakeholder
<ul>Users</ul>
<ul>Community</ul>


## Preconditions
A valid pom.xml file containing dependencies is needed to produce results.

## Success Scenario
If dependency tree structure is created, parsing license and other information into DB.

## Failure
Lack of tree structure, database and license information.

## Trigger 
A pom.xml is needed to initiate a success scenario.
