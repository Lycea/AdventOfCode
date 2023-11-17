


if [ "$#" -eq 3 ]
then
   echo "correct argument num"
   y=$1
   d=$2
else
    echo "wrong input argument number"
    echo "expected '<year> <day> <lang>'"
    exit
fi

echo "Creating new folder:" 

echo "   Using year $y"
echo "   Using day $d"

if [  -d "template/$3" ]
then
   echo "   Language exists: $3"
else
   echo "   Language does not exist: $3"
   exit
fi

#todo remove exit...

mkdir -p $y/$d
cp -r template/$3 $y/$d

