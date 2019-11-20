set -e

inputs=$(find data -name "*.in")

javac Levenshtein.java
for ifile in $inputs; do
  base=${ifile%.in}
  expfile=$base.ans
  actfile=$base.out
  java Levenshtein < $ifile > $actfile
  if ! diff $actfile $expfile; then
    echo "Test $base failed"
  fi
done
