FROM centos:centos6

RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum update -y
RUN yum install -y rpmdevtools git tar unzip readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libyaml libyaml-devel libffi libffi-devel

RUN mkdir -p /rpmbuild
ADD ./ /rpmbuild/
WORKDIR /rpmbuild
ENV HOME /

RUN wget -P /rpmbuild/SOURCES/ http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.gz
RUN chown root:root -R /rpmbuild

ENTRYPOINT ["/usr/bin/rpmbuild"]
CMD ["-bb","/rpmbuild/SPECS/ruby.spec"]
