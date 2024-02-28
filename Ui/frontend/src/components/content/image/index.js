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
        <div className='w-full flex justify-center'>
            <section className="w-[75%] flex-initial p-4 bg-slate-100 text-slate-400 rounded-lg border my-10">
                <div {...getRootProps({ className: 'dropzone' })}>
                    <input {...getInputProps()} />
                    <p>Drag 'n' drop some files here, or click to select files</p>
                    <em>1 image accepted</em>
                </div>
            </section>
        </div>
    );
    }

