%define rubyver         2.1.5
%define         prefix  /usr/local

Name:           ruby
Version:        %{rubyver}
Release:        2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libyaml libyaml-devel libffi libffi-devel
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 2.1
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel
Obsoletes: rubygems

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}

%build
rm -rf $RPM_BUILD_ROOT
CFLAGS="$RPM_OPT_FLAGS \
       -Wall -fno-strict-aliasing"
./configure --prefix=/usr/local \
  --exec-prefix=/usr/local \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir} \
  --enable-shared \
  --disable-rpath \
  --disable-install-doc \
  --without-X11 \
  $*
make %{?_smp_mflags}

%install
# installing binaries ...
make -e prefix=$RPM_BUILD_ROOT%{prefix} install

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
