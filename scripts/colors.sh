# ================================================================
# Terminal Colors for Script Output
# ================================================================
# Source this file: source scripts/colors.sh

# Standard Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[1;33m'
export BLUE='\033[0;34m'
export PURPLE='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[1;37m'
export NC='\033[0m'  # No Color

# Background Colors
export BG_RED='\033[0;41m'
export BG_GREEN='\033[0;42m'
export BG_YELLOW='\033[0;43m'
export BG_BLUE='\033[0;44m'

# Text Styles
export BOLD='\033[1m'
export UNDERLINE='\033[4m'
export ITALIC='\033[3m'

# Semantic Colors for Consistent Usage
export ERROR="$RED"
export SUCCESS="$GREEN"
export WARNING="$YELLOW"
export INFO="$BLUE"
export HIGHLIGHT="$PURPLE"

# Helper Functions
print_error() { echo -e "${ERROR}❌ $1${NC}"; }
print_success() { echo -e "${SUCCESS}✅ $1${NC}"; }
print_warning() { echo -e "${WARNING}⚠️  $1${NC}"; }
print_info() { echo -e "${INFO}ℹ️  $1${NC}"; }
print_highlight() { echo -e "${HIGHLIGHT}🔸 $1${NC}"; }
