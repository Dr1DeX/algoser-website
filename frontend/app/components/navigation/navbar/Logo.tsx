"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import Link from "next/link";


const Logo = () => {
    const [width, setWidth] = useState(0);

    const updateWidth = () => {
        const newWidth = window.innerWidth;
        setWidth(newWidth);
    };

    useEffect(() => {
        window.addEventListener('resize', updateWidth);
        updateWidth();
    }, []);

    return(
        <>
            <Link href='/' className="flex items-center space-x-3 rtl:space-x-reverse">
                <Image
                    src='/images/logo.png'
                    alt="Algoser logo"
                    className="relative"
                    width={width < 1024 ? "50" : "50"}
                    height={width < 1024 ? "50" : "50"}
                />
                <h1 className="text-3xl font-bold text-[hsl(205,40%,50%)]">
                    Algoser
            </h1>
            </Link>
        </>
    );
}

export default Logo