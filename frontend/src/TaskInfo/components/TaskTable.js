import React, { Component } from 'react';
import axios from 'axios';
import { Table, Tag, Space, Button } from 'antd';

export default class tasktable extends Component {
	constructor(props){
	    super(props);
		console.log(props)
		this.task_name = props.task_name
	    this.state={
	    	text:''
	    }
	  }
	
    componentWillMount(){
       let url = 'http://localhost:8000/task_allinfo/'+this.task_name;
        axios({
            method: 'get',
            url: url,
        }).then(res => {
			console.log(res.data)
            this.setState({
				info:res.data
            	// tasks:JSON.stringify(res.data.tasks)
            })
        }) 
    }
	
    componentDidMount(){
		// this.refresh()
    }
	refresh = () => {
		setInterval(() => {
			axios({
				method: 'get',
				url: 'http://localhost:8000/list_tasks',
			}).then(res => {
				console.log(res.data.tasks)
				this.setState({
					tasks:res.data.tasks
				})
			}) 
		}, 1000);		
	}

    render() {
		// const columns = []
		if (!this.state.info){
			return (
				<></>				
			) 
		}
		const columns = Object.keys(this.state.info).map(function (item) {
				return {
					title: item,
					dataIndex: item,
					key: item,
				};
		});
		var j = []
		for (var i=0;i<Object.keys(this.state.info).length;i++){
			j.push(<h1>{Object.keys(this.state.info)[i]} : {this.state.info[Object.keys(this.state.info)[i]]}</h1>) 
		}
        return (
			// <>{j}</>
	        <Table columns={columns} dataSource={[this.state.info]} />
			
		) 
	}
}
