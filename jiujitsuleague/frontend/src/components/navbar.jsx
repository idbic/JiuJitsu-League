import { Link } from 'react-router-dom';
import * as userService from '../../utilities/users-service'


export default function NavBar({user, setUser}) {
  //add the following function 
//   function handleLogOut(){
//     //Delegate to the user service
//     userService.logOut()
//     //Update state will also cause a re render
//     setUser(null)
//   }

  return (
    <nav>
      <Link to="/tournaments">Tournaments</Link>
      &nbsp; | &nbsp;
      <Link to="/profile">Profile</Link>
      &nbsp; | &nbsp;
      <Link to="/rankings">Rankings</Link>
      &nbsp; | &nbsp;
      Welcome, {user.name}
      &nbsp; | &nbsp;
      <Link to="" onClick={handleLogOut}>Loggity Logg Out Son!</Link>
      
    </nav>
  );
}