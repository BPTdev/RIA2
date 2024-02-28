
import Label from "../content/label";
import Image from "../content/image";

export default function Container({ children }) {
    return (
        <div className="w-full flex items-center justify-center">
            <div className="w-[40%] h-screen bg-slate-300">
                <div className="w-full mt-4 flex justify-end">
                    <div className=" flex w-24 gap-1 right-0">
                        <span className="text-underline">EN</span>
                        <span>FR</span>
                        <span>DE</span>
                    </div>
                </div>
                <h1 className="text-4xl mt-12" id="title">Img To Label</h1>
                <Image />
                <div className="separator w-full bg-black h-1"></div>
                <Label />
            </div>
        </div>
    );
    }