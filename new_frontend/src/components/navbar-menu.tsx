"use client";

import { useState } from 'react';
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ThemeToggle } from "@/components/ThemeToggle";
import { Menu } from "lucide-react";

export default function Component() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="fixed inset-x-0 top-0 z-50 bg-white shadow-sm dark:bg-gray-950/90">
      <div className="w-full max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-14 items-center">
          <h3>Schematics</h3>
          {/* Desktop Navigation */}
          <div className="hidden md:flex gap-4">
            <Link
              href="/"
              className="font-medium flex items-center text-sm transition-colors hover:underline"
              prefetch={false}
            >
              Home
            </Link>
            <Link
              href="/players"
              className="font-medium flex items-center text-sm transition-colors hover:underline"
              prefetch={false}
            >
              Players
            </Link>
            <Link
              href="/nba"
              className="font-medium flex items-center text-sm transition-colors hover:underline"
              prefetch={false}
            >
              NBA
            </Link>
            <Link
              href="about"
              className="font-medium flex items-center text-sm transition-colors hover:underline"
              prefetch={false}
            >
              About
            </Link>
          </div>
          {/* Mobile Menu Button */}
          <button
            className="md:hidden flex items-center"
            onClick={toggleMobileMenu}
          >
            <Menu className="h-6 w-6" />
          </button>

          {/* Mobile Menu */}
          {isMobileMenuOpen && (
            <div className="md:hidden absolute top-14 left-0 right-0 bg-white dark:bg-gray-950/90 shadow-sm z-50">
              <div className="flex flex-col gap-4 p-4">
                <Link
                  href="/"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  Home
                </Link>
                <Link
                  href="/players"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  Players
                </Link>
                <Link
                  href="/nba"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  NBA
                </Link>
                <Link
                  href="/about"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  About
                </Link>
              </div>
            </div>
          )}
          <div className="flex items-center gap-4">
            <ThemeToggle className="ml-4" />
          </div>
        </div>
      </div>
    </nav>
  );
}
