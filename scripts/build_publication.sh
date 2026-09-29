#!/bin/sh
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Giovanni Dalmasso and Joaquín Menacho
set -eu
cd "$(dirname "$0")/../src"
build_dir=${1:-build}
case "$build_dir" in *[!a-zA-Z0-9_-]*|'') echo 'Use a local output folder name.' >&2; exit 2;; esac
mkdir -p "$build_dir/texmf-var" "$build_dir/texmf-cache"
# Relative descendants are required by TeX's openout_any=p write policy.
export TEXMFVAR="./$build_dir/texmf-var"
export TEXMFCACHE="./$build_dir/texmf-cache"
for pass in 1 2 3; do
  lualatex --no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory="$build_dir" main.tex > "$build_dir/pass-$pass.stdout" 2>&1
done
