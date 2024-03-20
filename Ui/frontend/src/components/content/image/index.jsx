import React, {useEffect, useState} from 'react';
import {useDropzone} from 'react-dropzone';
import { useTranslation } from 'react-i18next';


export default function Image(props) {
    const { t } = useTranslation();
    const [files, setFiles] = useState([]);
    const {getRootProps, getInputProps} = useDropzone({
    accept: {
        'image/*': []
    },
    onDrop: acceptedFiles => {
        setFiles(acceptedFiles.map(file => Object.assign(file, {
        preview: URL.createObjectURL(file)
        })));
    }
    });
    
    const thumbs = files.map(file => (
    <div className='w-full mt-4' key={file.name}>
        <div>
        <img
        id='preview-image'
            alt='preview'
            className='w-full'
            src={file.preview}
            onLoad={() => { URL.revokeObjectURL(file.preview) }}
        />
        </div>
    </div>
    ));

    useEffect(() => {
    return () => files.forEach(file => URL.revokeObjectURL(file.preview));
    });

    return (
        <div>
            <div className='w-full flex justify-center'>
                    <section className="w-[75%] flex-initial p-4 bg-slate-100 text-slate-400 rounded-lg border my-10">
                        <div  {...getRootProps({ className: 'dropzone' })}>
                            <input {...getInputProps()} />
                            <p>{t('dragndroptext')}</p>
                            
                            <aside>
                                {thumbs}
                            </aside>
                        </div>
                    </section>
            </div>
            <div className='mb-10 w-full flex justify-center'>
                <div className='flex w-[75%] '>
                    <div>
                    <form className='text-left'>
                            <label htmlFor="numberInput">{t('max_labels')}</label>
                            <input className='ml-8 w-24 bg-slate-100' min={1} placeholder={5} type="number" id="numberInput" />
                            <br></br>
                            <br></br>
                            <label className='' htmlFor="numberInput">{t('min_confidence')}</label>
                            <input className='ml-8 w-24 bg-slate-100' max={100} min={1} placeholder={80} type="number" id="numberInput" />
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
}