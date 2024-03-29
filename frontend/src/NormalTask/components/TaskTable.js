import React, { Component } from 'react';
import axios from 'axios';
import { Table, Tag, Space, Button } from 'antd';
import PubSub from 'pubsub-js' 

export default class tasktable extends Component {
	constructor(props){
	    super(props);
	    this.state={
	    	tasks:[]
	    }
	  }
	
    componentWillMount(){
       let url = 'http://localhost:8000/list_tasks';
        axios({
            method: 'get',
            url: url,
        }).then(res => {
			console.log(res.data.tasks)
            this.setState({
				tasks:res.data.tasks
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
	run_task = (name) => {
        axios({
            method: 'get',
            url: 'http://localhost:8000/runtask_by_name/'+name,
        })
        axios({
            method: 'get',
            url: 'http://localhost:8000/list_tasks',
        }).then(res => {
			console.log(res.data.tasks)
            this.setState({
				tasks:res.data.tasks
            })
        }) 
	}

	stop_task = (name) => {
        axios({
            method: 'get',
            url: 'http://localhost:8000/stoptask_by_name/'+name,
        })
        axios({
            method: 'get',
            url: 'http://localhost:8000/list_tasks',
        }).then(res => {
			console.log(res.data.tasks)
            this.setState({
				tasks:res.data.tasks
            })
        }) 
	}

	task_info = (name) => {
		PubSub.publish('menu', name);
		this.setState({
			current: name,
		});
	}

    render() {
		const columns = [
		  {
		    title: '任务',
		    dataIndex: 'name',
		    key: 'name',
		    render: text => <a href={'http://localhost:8000/taskinfo/'+text}>{text}</a>,
		  },
		  {
		    title: '状态',
		    key: 'status',
		    dataIndex: 'status',
		    // render: tags => (
		    //   <>
		    //     {tags.map(tag => {
		    //       let color = tag.length > 5 ? 'geekblue' : 'green';
		    //       if (tag === 'loser') {
		    //         color = 'volcano';
		    //       }
		    //       return (
		    //         <Tag color={color} key={tag}>
		    //           {tag.toUpperCase()}
		    //         </Tag>
		    //       );
		    //     })}
		    //   </>
		    // ),
		  },
		  {
		    title: '开始时间',
			dataIndex: 'start_time',
		    key: 'start_time',
		  },
		  {
		    title: '停止时间',
			dataIndex: 'stop_time',
		    key: 'stop_time',

		  },
		  {
		    title: '异常',
		    dataIndex: 'exception',
		    key: 'exception',
		  },
		  
		  {
		    title: '运行',
			render: (text, record) => (
				<Button type="primary" id={record.name} onClick={()=>this.run_task(record.name)}>
					run
			  	</Button>
		    ),
		  },
		  {
		    title: '停止',
			render: (text, record) => (
				<Button type="primary" id={record.name} onClick={()=>this.stop_task(record.name)}>
					stop
			  	</Button>
		    ),
		  },
		  {
		    title: '详细信息',
			render: (text, record) => (
				<Button type="primary" id={record.name} onClick={()=>this.task_info(record.name)}>
					详细信息
			  	</Button>
		    ),
		  },
		];
        return (
			<div>
	        	<Table columns={columns} dataSource={this.state.tasks} />
			</div>
		) 
	}
}
