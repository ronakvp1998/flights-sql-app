use flights;
select * from fligUPDATE `flights`.`flights`

select distinct(source) from flights
union
select distinct(destination) from flights;

select airline,Route,Dep_Time,Duration,price from flights.flights
where Source = 'Banglore' and Destination = 'Delhi';

select Airline,count(*) from flights
group by Airline;

select distinct(source) from flights
union
select distinct(destination) from flights;

select source,count(*) from(
select source from flights
union All
select destination from flights) t
group by t.source;