Name:		jna
Version:	4.1.0
Release:	1
Summary:	JNA for Amazon Linux

License:	LGPL
URL:		https://github.com/marcelom/jnarpm
Source:		empty-jna-4.1.0.tar.gz

%description
This is the Java Native Access Library for Amazon Linux. Amazon does not provide JNA for their version of Linux, so here is a package to address this issue.

%prep
%setup -q

%files
/usr/share/java/jna.jar

%changelog
* Mon Mar 10 2014 Marcelo Moreira <marcelosm@gmail.com> 4.1.0-1
- 4.1.0 Binary packaging from https://github.com/twall/jna
