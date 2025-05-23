

function Message(){

    const name = 'amir';
    if (name)
        return <h1>Hello {name}</h1>;
        
    return <h1>no name</h1>;
}
export default Message;