"use client";

import React from "react";
import { useState } from "react";
import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import { ThemeToggle } from "@/components/ThemeToggle";
import { Menu } from "lucide-react";
import TestTubeIcon from "./icons/test-tube";
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";

export default function Component() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="fixed inset-x-0 top-0 z-50 border-b">
      <div className="w-full max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-14 items-center">
          {/* Logo: Link to Home */}
          <Link href="/" className="flex items-center gap-2" prefetch={false}>
            <TestTubeIcon color="text-primary" className="h-6 w-6" />
            <span className="text-lg font-semibold">Sports Predictions</span>
          </Link>
          {/* Desktop Navigation */}
          <div className="hidden md:flex gap-4">
            {/* Link to Home */}
            <Link
              href="/"
              className={buttonVariants({ variant: "ghost" })}
              prefetch={false}
            >
              Home
            </Link>
            {/* Drop Down for NBA */}
            <NavigationMenu>
              <NavigationMenuList>
                <NavigationMenuItem>
                  <NavigationMenuTrigger>NBA</NavigationMenuTrigger>
                  <NavigationMenuContent>
                    {/* Link to NBA Player Page */}
                    <Link href="/nba/players" prefetch={false}>
                      <NavigationMenuLink
                        className={navigationMenuTriggerStyle()}
                      >
                        Players
                      </NavigationMenuLink>
                    </Link>
                    {/* Link to NBA Team Page */}
                    <Link href="/nba/teams" prefetch={false}>
                      <NavigationMenuLink
                        className={navigationMenuTriggerStyle()}
                      >
                        Teams
                      </NavigationMenuLink>
                    </Link>
                  </NavigationMenuContent>
                </NavigationMenuItem>
              </NavigationMenuList>
            </NavigationMenu>
            {/* Link to About */}
            <Link
              href="/about"
              // className="font-medium flex items-center text-sm transition-colors hover:underline"
              className={buttonVariants({ variant: "ghost" })}
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
                {/* Link to Home */}
                <Link
                  href="/"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  Home
                </Link>
                {/* Link to Players */}
                <Link
                  href="/nba/players"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  Players
                </Link>
                {/* Link to NBA */}
                <Link
                  href="/nba"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  NBA
                </Link>
                {/* Link to About */}
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
