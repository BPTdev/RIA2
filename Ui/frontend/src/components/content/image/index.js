import {useDropzone} from 'react-dropzone';
    
export default function Image() {
    const {
        acceptedFiles,
        fileRejections,
        getRootProps,
        getInputProps
    } = useDropzone({    
        maxFiles:1,
        accept: 'image/*'
    });
    
    const acceptedFileItems = acceptedFiles.map(file => (
        <li key={file.path}>
        {file.path} - {file.size} bytes
        </li>
    ));
    
    const fileRejectionItems = fileRejections.map(({ file, errors  }) => { 
    return (
        <li key={file.path}>
            {file.path} - {file.size} bytes
            <ul>
                {errors.map(e => <li key={e.code}>{e.message}</li>)}
            </ul>
    
        </li>
    ) 
    });
    
    
    return (
        <div>
            <div className='w-full flex justify-center'>
                <section className="w-[75%] flex-initial p-4 bg-slate-100 text-slate-400 rounded-lg border my-10">
                    <div {...getRootProps({ className: 'dropzone' })}>
                        <input {...getInputProps()} />
                        <p>Drag 'n' drop some files here, or click to select files</p>
                        <em>Only 1 image</em>
                    </div>
                    
                    
                </section>
                
            </div>
            <div className='mb-10 w-full flex justify-center'>
                <div className='flex w-[75%] '>
                    <div>
                    <form className='text-left'>
                            <label htmlFor="numberInput">Max labels:</label>
                            <input className='ml-8 w-24 bg-slate-100' placeholder='Number' min={1} value={5} type="number" id="numberInput" />
                            <br></br>
                            <br></br>
                            <label className='' htmlFor="numberInput">Min confidence:</label>
                            <input className='ml-8 w-24 bg-slate-100' placeholder='Number' max={100} min={1} value={80} type="number" id="numberInput" />
                        </form>
                    </div>
                </div>
        </div>
    </div>
    );
    }

