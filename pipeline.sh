
if [[ $1 = "filter" ]]
then
    python3 filters.py -i archive/pp-2017.csv -i archive/pp-2016-part1.csv -i archive/pp-2016-part2.csv -i archive/pp-2015-part1.csv -i archive/pp-2015-part2.csv -f LONDON
fi;

if [[ $1 = "visualize" ]]
then
    python3 visualize.py -i data/houses.csv
fi;

