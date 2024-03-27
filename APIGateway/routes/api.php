<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;


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

Route::post('/test', function (Request $request) {
    
    if ($request->hasFile('image') && $request->file('image')->isValid()) {
        $response = Http::attach(
            'file',
            file_get_contents($request->image->path()),
            $request->image->getClientOriginalName()
        )->post('http://localhost:5171/analyze');
        return response()->json($response->json());
    } else {
        return response()->json(['error' => 'No valid image provided'], 400);
    }
});
