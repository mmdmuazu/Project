import { useState } from "react";
import './index.css'
function ListGroup() {
  let items = ["shadda", "yadi", "atamfa", "hula"];
  const [selectedIndex] = useState(0);
  function test(input:string){
    fetch('http://127.0.0.1:5000/update_balance',{
      method:'POST',
      headers: {
        'Content-Type':'application',
        // 'X-CSRFToken':
      },
      body:JSON.stringify({data:input})
    })
    .then(response => response.json)
    .then(data => {
      const a = console.log(data);
      return a;
    })
  }

  return (
    <>
      <h1 className='h1'>heading</h1>
      {items.length === 0 && <p>no items found</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={()=>test(item)}
            // onClick={() => setSelectedIndex(index)}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
