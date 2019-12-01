set -e

inputs=$(find data -name "*.in")

for ifile in $inputs; do
  base=${ifile%.in}
  expfile=$base.ans
  actfile=$base.out
  python fixedpoint.py < $ifile > $actfile
  if ! diff $actfile $expfile; then
    echo "Test $base failed"
  fi
done
