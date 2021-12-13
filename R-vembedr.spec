#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vembedr
Version  : 0.1.5
Release  : 2
URL      : https://cran.r-project.org/src/contrib/vembedr_0.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vembedr_0.1.5.tar.gz
Summary  : Embed Video in HTML
Group    : Development/Tools
License  : MIT
Requires: R-assertthat
Requires: R-glue
Requires: R-htmltools
Requires: R-httr
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-stringr
BuildRequires : R-assertthat
BuildRequires : R-conflicted
BuildRequires : R-glue
BuildRequires : R-htmltools
BuildRequires : R-httr
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
embed hosted video in your R Markdown documents or Shiny applications.

%prep
%setup -q -c -n vembedr
cd %{_builddir}/vembedr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639425574

%install
export SOURCE_DATE_EPOCH=1639425574
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vembedr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vembedr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library vembedr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc vembedr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vembedr/DESCRIPTION
/usr/lib64/R/library/vembedr/INDEX
/usr/lib64/R/library/vembedr/LICENSE
/usr/lib64/R/library/vembedr/Meta/Rd.rds
/usr/lib64/R/library/vembedr/Meta/features.rds
/usr/lib64/R/library/vembedr/Meta/hsearch.rds
/usr/lib64/R/library/vembedr/Meta/links.rds
/usr/lib64/R/library/vembedr/Meta/nsInfo.rds
/usr/lib64/R/library/vembedr/Meta/package.rds
/usr/lib64/R/library/vembedr/Meta/vignette.rds
/usr/lib64/R/library/vembedr/NAMESPACE
/usr/lib64/R/library/vembedr/NEWS.md
/usr/lib64/R/library/vembedr/R/vembedr
/usr/lib64/R/library/vembedr/R/vembedr.rdb
/usr/lib64/R/library/vembedr/R/vembedr.rdx
/usr/lib64/R/library/vembedr/doc/embed.R
/usr/lib64/R/library/vembedr/doc/embed.Rmd
/usr/lib64/R/library/vembedr/doc/embed.html
/usr/lib64/R/library/vembedr/doc/index.html
/usr/lib64/R/library/vembedr/doc/modify.R
/usr/lib64/R/library/vembedr/doc/modify.Rmd
/usr/lib64/R/library/vembedr/doc/modify.html
/usr/lib64/R/library/vembedr/doc/vembedr.R
/usr/lib64/R/library/vembedr/doc/vembedr.Rmd
/usr/lib64/R/library/vembedr/doc/vembedr.html
/usr/lib64/R/library/vembedr/help/AnIndex
/usr/lib64/R/library/vembedr/help/aliases.rds
/usr/lib64/R/library/vembedr/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/vembedr/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/vembedr/help/paths.rds
/usr/lib64/R/library/vembedr/help/vembedr.rdb
/usr/lib64/R/library/vembedr/help/vembedr.rdx
/usr/lib64/R/library/vembedr/html/00Index.html
/usr/lib64/R/library/vembedr/html/R.css
/usr/lib64/R/library/vembedr/tests/testthat.R
/usr/lib64/R/library/vembedr/tests/testthat/test-div.R
/usr/lib64/R/library/vembedr/tests/testthat/test-iframe.R
/usr/lib64/R/library/vembedr/tests/testthat/test-misc.R
/usr/lib64/R/library/vembedr/tests/testthat/test-secs-hms.R
/usr/lib64/R/library/vembedr/tests/testthat/test-suggest.R
/usr/lib64/R/library/vembedr/tests/testthat/test-use_start_time.R
/usr/lib64/R/library/vembedr/vembedr/css/vembedr.css
