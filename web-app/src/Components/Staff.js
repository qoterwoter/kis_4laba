import React from 'react';
import ApiService from '../Api/ApiService'

const link = 'staff';
const apiService = new ApiService();

export default class Staff extends React.Component { 

    constructor(props) {
        super(props)

        this.state={
            staff:[]
        }
    }

    componentDidMount() {
        apiService.getDatas(link).then(response=>{
            this.setState({staff:response.data})
            console.log(response.data)
        })
    }
    
    render(){
    return(
        <div className='staff'>
            <h2>Новости для персонала</h2>
            <div className='staff'>
                {this.state.staff.map((newz)=>
                    <div className='staff__block block'>
                        <h4 className='block__title'>{newz.title}</h4>
                        <p className='block__description'>{newz.description}</p>
                        <img className='block__image' src={newz.photo} alt='no description'/>
                        <p className='block__author'>Автор: <i>{newz.user}</i></p>
                        <p className='block__date'>Опубликовано: {newz.date}</p>
                    </div>
                )}
            </div>
        </div>
    )}
}