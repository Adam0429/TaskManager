import React, { Component } from 'react';
import axios from 'axios';
import { Table, Tag, Space, Button } from 'antd';

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
        
    // componentDidMount(){
    //     var myChart = echarts.init(document.getElementById("pie"),'dark');
    //     var option;

    //     option = {
    //         title: {
    //             text: '用户订单',
    //             x: 'center'
    //         },
    //         tooltip : {
    //             trigger: 'item',
    //             //提示框浮层内容格式器，支持字符串模板和回调函数形式。
    //             formatter: "{a} <br/>{b} : {c} ({d}%)" 
    //         },
    //         // legend: {
    //         //     orient: 'vertical',
    //         //     top: 20,
    //         //     right: 5,
    //         //     data: ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    //         // },
    //         series : [
    //             {
    //                 name:'订单量',
    //                 type:'pie',
    //                 data:[
    //                     {value:2000, name:'星期一'},
    //                     {value:1500, name:'星期二'},
    //                     {value:2000, name:'星期三'},
    //                     {value:2500, name:'星期四'},
    //                     {value:3000, name:'星期五'},
    //                     {value:2300, name:'星期六'},
    //                     {value:1600, name:'星期日'}
    //                 ].sort(function (a, b) { return a.value - b.value; }),
    //                 roseType: 'radius'
    //             }
    //         ],
    //     }
    //     myChart.setOption(option);
    // }
	enterLoading = index => {
		this.setState(({ loadings }) => {
		  const newLoadings = [...loadings];
		  newLoadings[index] = true;
	
		  return {
			loadings: newLoadings,
		  };
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
				<Button type="primary" id={record.name} onClick={() => alert('ouch')}>
					run
			  	</Button>
				// <form action="http://localhost:8000/runtask_by_name" method="POST">
				// 	<input type="hidden" name="task_name" value= {record.name}/>
				// 	<input type="submit" value="runtask"></input>
				// </form>
		    ),
		  },

		  {
		    title: '停止',
			render: (text, record) => (
				<form action="http://localhost:8000/stoptask_by_name" method="POST">
					<input type="hidden" name="task_name" value={record.name}/>
					<input type="submit" value="stoptask"></input>
				</form>
		    ),
		  },
		];

		// const data = [
		//   {
		//     key: '1',
		//     name: 'John Brown',
		//     age: 32,
		//     address: 'New York No. 1 Lake Park',
		//     tags: ['nice', 'developer'],
		//   },
		//   {
		//     key: '2',
		//     name: 'Jim Green',
		//     age: 42,
		//     address: 'London No. 1 Lake Park',
		//     tags: ['loser'],
		//   },
		//   {
		//     key: '3',
		//     name: 'Joe Black',
		//     age: 32,
		//     address: 'Sidney No. 1 Lake Park',
		//     tags: ['cool', 'teacher'],
		//   },
		// ];
        return (
        	<div>
        		{/* <h1>{this.state.tasks}</h1> */}
	        	<Table columns={columns} dataSource={this.state.tasks} />
        	</div>)
        
	}
}
