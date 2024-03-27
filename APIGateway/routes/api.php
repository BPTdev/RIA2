<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Storage;
use App\Helpers\ConversionHelper;


/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});


Route::get('/mock', function (Request $request) {
    return response()->json(Storage::get('response.json'));
});

Route::get('/analyze', function (Request $request) {
    $contents = Storage::get('response.json');
    $mock = json_decode($contents, true);
    $temp = [];

    foreach ($mock['Labels'] as $label) {
        $temp[] = [
            'name' => $label['Name'],
            'confidence' => $label['Confidence'],
        ];
    }

    return response()->json($temp);
});

Route::get('/sequence', function (Request $request) {
    
    $data = ConversionHelper::convertToJsonForUi($jsonString);
});

