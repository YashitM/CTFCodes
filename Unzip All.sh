#!/bin/bash

filename="26685"
i=0
archive_name="archivename"
unpacked=false


unpack_nufile() {
    file $archive_name | grep "NuFile archive"
    if [ $? -eq 0 ]; then
        ./nulib/nulib x $archive_name
        unpacked=true
    fi
}

unpack_bzip2() {
    file $archive_name | grep "bzip2 compressed data"
    if [ $? -eq 0 ]; then
        bzip2 -d $archive_name
        mv $archive_name.out $filename
        unpacked=true
    fi
}

unpack_zoo() {
    file $archive_name | grep "Zoo archive data"
    if [ $? -eq 0 ]; then
        mv $archive_name $archive_name.zoo
        zoo -extract $archive_name.zoo
        mv $archive_name $filename
        unpacked=true
    fi
}

unpack_lzip() {
    file $archive_name | grep "lzip compressed data"
    if [ $? -eq 0 ]; then
        lzip -d $archive_name
        mv $archive_name.out $filename
        unpacked=true
    fi
}

unpack_gzip() {
    file $archive_name | grep "gzip compressed data"
    if [ $? -eq 0 ]; then
        mv $archive_name $archive_name.gz
        gzip -d $archive_name.gz
        unpacked=true
    fi
}
unpack_tar() {
    file $archive_name | grep "POSIX tar archive (GNU)"
    if [ $? -eq 0 ]; then
        tar xvf $archive_name
        unpacked=true
    fi
}


unpack_7z() {
    file $archive_name | grep "7-zip archive data"
    if [ $? -eq 0 ]; then
        7za e $archive_name
        unpacked=true
    fi
}

unpack_zpaq() {
    file $archive_name | grep "ZPAQ stream, level 1"
    if [ $? -eq 0 ]; then
        zpaq x $archive_name
        unpacked=true
    fi
}

unpack_zip() {
    file $archive_name | egrep "Zip (compressed|archive) data"
    if [ $? -eq 0 ]; then
        mv $archive_name $archive_name.zip
        unzip $archive_name.zip
        unpacked=true
    fi
}

unpack_7z() {
    file $archive_name | grep "7-zip archive data"
    if [ $? -eq 0 ]; then
        7za e $archive_name
        unpacked=true
    fi
}

unpack_lzma() {
    file $archive_name | grep "LZMA compressed data"
    if [ $? -eq 0 ]; then
        mv $archive_name $archive_name.lzma
        unlzma $archive_name.lzma
        mv $archive_name $filename
        unpacked=true
    fi
}

unpack_arj() {
    file $archive_name | grep "ARJ archive data"
    if [ $? -eq 0 ]; then
        mv $archive_name $archive_name.arj
        arj e $archive_name
        unpacked=true
    fi
}

unpack_xz() {
    file $archive_name | grep "XZ compressed data"
    if [ $? -eq 0 ]; then
        mv $archive_name $archive_name.xz
        xz -d $archive_name.xz
        mv $archive_name $fn
        unpacked=true
    fi
}

unpack_zpaq() {
    file $archive_name | grep "ZPAQ stream, level 1"
    if [ $? -eq 0 ]; then
        zpaq x $archive_name
        unpacked=true
    fi
}


while true; do
    mv $filename $archive_name
    unpack_nufile
    unpack_bzip2
    unpack_zoo
    unpack_lzip
    unpack_zip
    unpack_7z
    unpack_zpaq
    unpack_gzip
    unpack_tar
    unpack_arj
    unpack_lzma
    unpack_xz

    if $unpacked; then
        i=$((i+1))
        echo "unpacked $i"
    else
        exit 0
    fi
    unpacked=false
done