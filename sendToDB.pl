
#!/usr/bin/perl

use DBI;

@ARGV > 0 or die "Usage: perl sendToDB.pl file_to_scan \n NOTE: Must be root user!";

my $fileToScan = $ARGV[0];
my $command = "./nomos $fileToScan";
my @nomosResults = `$command`;

# database stuff
my $driver = "mysql";
my $database = "nomosResults";
my $dsn = "DBI:$driver:database=$database";
my $userid = "your_user_id_or_root";
my $password = "your_password";
my $host = "localhost";
my $dbh = DBI->connect($dsn, $userid, $password) or die $DBI::errstr;

foreach my $fileScanned (@nomosResults){
	my ($filename, $licenses) = ($fileScanned =~ /File (.*) contains license\(s\) (.*)/);

	my $sqlQuery = $dbh->prepare("insert into nomosResultsTable (filename, license) values ('$filename', '$licenses')");
	$sqlQuery->execute() or die $DBI::errstr;
	$sqlQuery->finish();
}

exit(0);
