import React, { useState } from 'react'; // Import useState
import Label from "../content/label";
import Image from "../content/image";
import { useTranslation } from 'react-i18next';
import i18n from '../../translations/i18n';

export default function Container({ children }) {
    const { t } = useTranslation();
    const [data, setData] = useState(''); // State to store fetched data

    const changeLanguage = (language) => {
        i18n.changeLanguage(language);
    };


    const fetchData = async (url) => {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setData(data);
            })
            .catch(error => {
                console.error('Error:', error);
                setData(null); // or set to an appropriate error state
            });
    };


    // Handler for the Start button click
    const handleStartClick = () => {
        fetchData('/analyze');
    };

    const handleDeleteLabels = () => {
        setData('');
    }


    return (
        <div className="w-full flex items-center justify-center">
            <div className="w-[40%] h-screen">
                <div className="w-full mt-4 flex justify-end">
                    <div className=" flex w-24 gap-1 right-0">
                        <button id='lang-en' onClick={() => changeLanguage('en')}><span>EN</span></button>
                        <button id='lang-fr' onClick={() => changeLanguage('fr')}><span>FR</span></button>
                        <button id='lang-de' onClick={() => changeLanguage('de')}><span>DE</span></button>
                    </div>
                </div>
                <h1 className="text-4xl mt-12" id="title">{t('title')}</h1>
                <Image />
                <div className="w-full flex justify-center">
                    <div className="separator w-[75%] bg-black h-1"></div>
                </div>

                <Label response={data} />
                <div className="w-full flex justify-center mt-10">
                    <div className="cursor-pointer h-12 text-center justify-center w-[75%] rounded-xl bg-lime-500">
                        <div onClick={handleStartClick} className="p-3 text-xl">Start</div>
                        <div className='flex'>
                            <div className='flex-1'></div>
                            <div className='mt-2 cursor-pointer rounded-md bg-gray-100 py-2 w-2/4 border' onClick={handleDeleteLabels}><p>{t('delete_labels')}</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
