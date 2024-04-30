#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Update and upgrade apt packages
echo "Updating and upgrading apt packages..."
apt update && apt upgrade -y

# Install wget if not already installed
echo "Installing wget..."
apt install wget -y

# Download Bazelisk binary for ARM64
echo "Downloading Bazelisk for ARM64..."
wget https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-arm64 -O /usr/local/bin/bazelisk

# Make Bazelisk executable
echo "Making Bazelisk executable..."
chmod +x /usr/local/bin/bazelisk

# Optionally, link bazelisk to bazel to use it as the default bazel command
echo "Linking Bazelisk to Bazel..."
ln -s /usr/local/bin/bazelisk /usr/local/bin/bazel

# Check Bazelisk version
echo "Bazelisk installation completed. Checking version..."
bazelisk version
