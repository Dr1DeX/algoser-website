"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import Link from "next/link";
import Button from "./Button";


const Logo = () => {
    const [width, setWidth] = useState(0)

    const updateWidth = () => {
        const newWidth = window.innerWidth;
        setWidth(newWidth);
    };

    useEffect(() => {
        window.addEventListener('resize', updateWidth);
        updateWidth();
    }, []);

    const [showButton, setShowButton] = useState(false);

    const changeNavButton = () => {
        if (window.scrollY >= 400 && window.innerWidth < 768) {
            setShowButton(true);
        } else {
            setShowButton(false);
        }
    };

    useEffect(() => {
        window.addEventListener('scroll', changeNavButton);
    }, []);

    return(
        <>
            <Link href="/" className="mx-2 my-1 flex items-center lg:mb-0 lg:mt-0">
                <Image
                src="/images/logo.png"
                alt="Logo"
                width={width < 1024 ? "40" : "40"}
                height={width < 1024 ? "40" : "40"}
                className="relative me-4"
                />
                <p className="bg-gradient-to-r from-purple-500 to-red-300 bg-clip-text text-transparent text-lg">Algoser</p>
            </Link>
            <div
                style={{
                    display: showButton ? "block" : "none",
                }}
            >
                <Button />
            </div>
        </>
    )
}

export default Logo;