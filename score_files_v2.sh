#!/bin/bash
# Enhanced Document Scoring Script v2.0
# Scores all MD files and categorizes PDFs for manual review
# Output: CSV format for analysis

RESEARCH_DIR="/home/user/GitHub-CDM-Research/Research Documentation"
OUTPUT_FILE="/home/user/GitHub-CDM-Research/Research Documentation/AUTOMATED-SCORES.csv"

# Exclusion patterns
is_excluded() {
    local file="$1"

    # Versioned duplicates (keep only docs/ or latest version)
    if [[ "$file" == *"versioned_docs/version-5.13.0"* ]] || \
       [[ "$file" == *"versioned_docs/version-5.20.0"* ]]; then
        echo "VERSIONED_DUPLICATE"
        return 0
    fi

    # Internal tech docs
    if [[ "$file" == *".junie/xtend-docs"* ]]; then
        echo "INTERNAL_TECH"
        return 0
    fi

    # GitHub templates
    if [[ "$file" == *"ISSUE_TEMPLATE"* ]] || \
       [[ "$file" == *"pull_request_template"* ]] || \
       [[ "$file" == *"CODE_OF_CONDUCT.md" ]]; then
        echo "GITHUB_TEMPLATE"
        return 0
    fi

    # License files
    if [[ "$file" == *"LICENSE.md" ]] || \
       [[ "$file" == *"NOTICE.md" ]] || \
       [[ "$file" == *"license-terms"* ]] || \
       [[ "$file" == *"EASYCLA"* ]]; then
        echo "LICENSE_FILE"
        return 0
    fi

    # Logo/asset files
    if [[ "$file" == *"logo"* ]] || [[ "$file" == *"Logo"* ]]; then
        echo "ASSET_FILE"
        return 0
    fi

    echo "INCLUDE"
    return 1
}

# Determine tier from path
get_tier() {
    local file="$1"
    if [[ "$file" == *"Tier 1"* ]]; then echo "1"
    elif [[ "$file" == *"Tier 2"* ]]; then echo "2"
    elif [[ "$file" == *"Tier 3"* ]]; then echo "3"
    elif [[ "$file" == *"Tier 4"* ]]; then echo "4"
    elif [[ "$file" == *"Tier 5"* ]]; then echo "5"
    elif [[ "$file" == *"Tier 6"* ]]; then echo "6"
    else echo "TOP"
    fi
}

# Determine category from path
get_category() {
    local file="$1"
    if [[ "$file" == *"CDM Documentation"* ]]; then
        if [[ "$file" == *"Technical"* ]]; then echo "CDM_TECHNICAL"
        else echo "CDM_NON_TECHNICAL"
        fi
    elif [[ "$file" == *"Broader Industry"* ]]; then echo "INDUSTRY_CONTEXT"
    else echo "OTHER"
    fi
}

# Score a single MD file
score_md_file() {
    local file="$1"

    # Keyword scoring (weighted)
    local banks=$(grep -cioE "JPMorgan|Goldman|Citi|Bank of America|Morgan Stanley|Wells Fargo|BNP Paribas|JSCC|Barclays|Standard Chartered|Deutsche Bank|UBS|HSBC|Credit Suisse|Pictet" "$file" 2>/dev/null || echo 0)
    local production=$(grep -cioE "production|go-live|deployed|implemented|live environment" "$file" 2>/dev/null || echo 0)
    local quant=$(grep -cioE "[0-9]+%|billion|million|\\\$[0-9]+|savings|reduction|cost|efficiency" "$file" 2>/dev/null || echo 0)
    local strategic=$(grep -cioE "strategy|architecture|integration|native|translation|semi-native|adoption|roadmap" "$file" 2>/dev/null || echo 0)
    local regulatory=$(grep -cioE "CFTC|FDTA|mandate|requirement|compliance|EMIR|MiFIR|ASIC|MAS|JFSA|ESMA|FCA|SEC|HKMA|CSA" "$file" 2>/dev/null || echo 0)
    local recent=$(grep -cioE "202[45]|January 2025|February 2025|October 2025|December 2025" "$file" 2>/dev/null || echo 0)
    local impl=$(grep -cioE "case study|implementation|adoption|pilot|proof of concept|POC" "$file" 2>/dev/null || echo 0)

    # New categories for gap analysis
    local asset_class=$(grep -cioE "repo|securities lending|ICMA|ISLA|GMSLA|GMRA|collateral|bonds" "$file" 2>/dev/null || echo 0)
    local smart_contract=$(grep -cioE "smart contract|tokenization|tokenovate|DAML|DLT|blockchain|digital asset" "$file" 2>/dev/null || echo 0)
    local training=$(grep -cioE "training|certification|workforce|skills|course|learning" "$file" 2>/dev/null || echo 0)

    # Calculate weighted score
    local score=$((banks*5 + production*4 + quant*3 + strategic*3 + regulatory*3 + recent*2 + impl*3 + asset_class*2 + smart_contract*3 + training*1))

    echo "$banks|$production|$quant|$strategic|$regulatory|$recent|$impl|$asset_class|$smart_contract|$training|$score"
}

# Main execution
echo "file_path|file_type|tier|category|exclusion_status|banks|production|quant|strategic|regulatory|recent|impl|asset_class|smart_contract|training|raw_score|priority_tier" > "$OUTPUT_FILE"

cd "$RESEARCH_DIR"

find . -type f \( -name "*.md" -o -name "*.pdf" \) | while read -r file; do
    # Get file type
    if [[ "$file" == *.pdf ]]; then
        file_type="PDF"
    else
        file_type="MD"
    fi

    # Get metadata
    tier=$(get_tier "$file")
    category=$(get_category "$file")
    exclusion=$(is_excluded "$file")

    # Score file (only MD files for now)
    if [[ "$file_type" == "MD" ]] && [[ "$exclusion" == "INCLUDE" ]]; then
        scores=$(score_md_file "$file")
        raw_score=$(echo "$scores" | cut -d'|' -f11)

        # Determine priority tier based on score
        if [ "$raw_score" -ge 100 ]; then
            priority="S"
        elif [ "$raw_score" -ge 50 ]; then
            priority="A"
        elif [ "$raw_score" -ge 20 ]; then
            priority="B"
        elif [ "$raw_score" -ge 5 ]; then
            priority="C"
        else
            priority="D"
        fi

        echo "$file|$file_type|$tier|$category|$exclusion|$scores|$priority" >> "$OUTPUT_FILE"
    elif [[ "$file_type" == "PDF" ]] && [[ "$exclusion" == "INCLUDE" ]]; then
        # PDF files need manual review - mark with placeholder scores
        echo "$file|$file_type|$tier|$category|$exclusion|0|0|0|0|0|0|0|0|0|0|0|MANUAL_REVIEW" >> "$OUTPUT_FILE"
    else
        # Excluded files
        echo "$file|$file_type|$tier|$category|$exclusion|0|0|0|0|0|0|0|0|0|0|0|EXCLUDED" >> "$OUTPUT_FILE"
    fi
done

echo "Scoring complete. Results saved to: $OUTPUT_FILE"

# Summary statistics
echo ""
echo "=== SUMMARY ==="
total=$(tail -n +2 "$OUTPUT_FILE" | wc -l)
excluded=$(grep -c "EXCLUDED" "$OUTPUT_FILE")
manual=$(grep -c "MANUAL_REVIEW" "$OUTPUT_FILE")
tier_s=$(grep -c "|S$" "$OUTPUT_FILE")
tier_a=$(grep -c "|A$" "$OUTPUT_FILE")
tier_b=$(grep -c "|B$" "$OUTPUT_FILE")
tier_c=$(grep -c "|C$" "$OUTPUT_FILE")
tier_d=$(grep -c "|D$" "$OUTPUT_FILE")

echo "Total files: $total"
echo "Excluded: $excluded"
echo "PDFs (manual review): $manual"
echo "Priority S (100+): $tier_s"
echo "Priority A (50-99): $tier_a"
echo "Priority B (20-49): $tier_b"
echo "Priority C (5-19): $tier_c"
echo "Priority D (<5): $tier_d"
