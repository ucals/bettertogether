% include('header.tpl')
<div class="container">
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <h1 class="text-center">#bettertogether</h1>
            <br/>
            <p class="lead text-center">We couldn't find {{student}}'s assignment {{assignment}}<p>
            <p class="lead text-center"><a role="button" class="btn btn-outline-primary btn-lg" href="javascript:history.back()">Go Back!</a><p>
            % include('credit.tpl')
        </div>
    </div>
</div>
% include('footer.tpl')