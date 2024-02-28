
import Label from "../content/label";
import Image from "../content/image";

export default function Container({ children }) {
    return (
        <div className="w-full flex items-center justify-center">
            <div className="w-[40%] h-screen">
                <div className="w-full mt-4 flex justify-end">
                    <div className=" flex w-24 gap-1 right-0">
                        <span className="text-underline">EN</span>
                        <span>FR</span>
                        <span>DE</span>
                    </div>
                </div>
                <h1 className="text-4xl mt-12" id="title">Img To Label</h1>
                <Image />
                <div className="w-full flex justify-center">
                    <div className="separator w-[75%] bg-black h-1"></div>
                </div>
                
                <Label />
                <div className="w-full flex justify-center mt-10">
                    <div className="h-12 text-center justify-center w-[75%] rounded-xl bg-lime-500">
                        <p className="p-3 text-xl">Start</p>
                    </div>
                </div>
            </div>
        </div>
    );
    }