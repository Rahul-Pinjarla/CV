const RedText = ({text}) => {
    return <span style={{color: 'red'}}>{text}</span>
}

const App = () => {

    const [text, setText] = useState('');
    const [counter, setCounter] = useState(0);

    useEffect(
        //function
        () => {
            const fetchData = async () => {
                setCounter(counter+1);
                console.log(counter)
            }
            fetchData();
        },
        //dependencies
        [text]
    )

    return (
        <>
        <input name="text" value={text} onChange={(e) => setText(e.target.value)}/>
        <RedText>{text}</RedText>
        </>
    )
}