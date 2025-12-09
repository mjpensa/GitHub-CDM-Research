#!/bin/bash
cd "/home/user/GitHub-CDM-Research/Research Documentation"

score_file() {
    local file="$1"
    local banks=$(grep -ioE "JPMorgan|Goldman|Citi|Bank of America|Morgan Stanley|Wells Fargo|BNP Paribas|JSCC|Barclays|Standard Chartered" "$file" 2>/dev/null | wc -l)
    local production=$(grep -ioE "production|go-live|deployed|implemented|live" "$file" 2>/dev/null | wc -l)
    local quant=$(grep -ioE "[0-9]+%|billion|million|savings|reduction|cost" "$file" 2>/dev/null | wc -l)
    local strategic=$(grep -ioE "strategy|architecture|integration|native|translation|semi-native" "$file" 2>/dev/null | wc -l)
    local regulatory=$(grep -ioE "CFTC|FDTA|mandate|requirement|compliance|EMIR|MiFIR|ASIC|MAS|JFSA" "$file" 2>/dev/null | wc -l)
    local recent=$(grep -ioE "2025|2024" "$file" 2>/dev/null | wc -l)
    local impl=$(grep -ioE "case study|implementation|adoption|pilot|proof of concept" "$file" 2>/dev/null | wc -l)

    local score=$((banks*5 + production*4 + quant*3 + strategic*3 + regulatory*3 + recent*2 + impl*2))

    if [ $score -gt 5 ]; then
        echo "$score|$file|B:$banks|P:$production|Q:$quant|S:$strategic|R:$regulatory|D:$recent|I:$impl"
    fi
}

# Score all MD files
find . -type f -name "*.md" -print0 2>/dev/null | while IFS= read -r -d '' file; do
    score_file "$file"
done | sort -t'|' -k1 -nr
