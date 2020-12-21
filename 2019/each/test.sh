set -e

inputs=$(find data -name "*.in")

for ifile in $inputs; do
  base=${ifile%.in}
  expfile=$base.ans
  actfile=$base.out
  python each.py < $ifile > $actfile
  if ! cmp $actfile $expfile; then
    echo "Test $base failed"
  fi
done
