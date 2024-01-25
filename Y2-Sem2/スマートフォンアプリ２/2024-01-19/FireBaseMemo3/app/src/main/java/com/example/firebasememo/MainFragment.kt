package com.example.firebasememo

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.inputmethod.InputMethodManager
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.firebasememo.databinding.FragmentMainBinding
import com.google.android.gms.tasks.Task
import com.google.android.material.snackbar.Snackbar
import com.google.firebase.firestore.CollectionReference
import com.google.firebase.firestore.DocumentSnapshot
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.ListenerRegistration
import com.google.firebase.firestore.Query
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.firestore.ktx.toObject
import com.google.firebase.ktx.Firebase

// メインのフラグメントクラスです。メモを表示、追加、更新する役割を持っています。
class MainFragment : Fragment(), MemoListener {

    // -------------------------プロパティの宣言部分

    // Firestoreのインスタンス
    private lateinit var firestore : FirebaseFirestore
    // Firestoreのクエリ
    private var query: Query? = null
    // ViewBindingのインスタンス
    private lateinit var binding: FragmentMainBinding
    // メモのアダプター
    private var adapter: MemoAdapter? = null

    private var registration:ListenerRegistration? = null

    // ログに表示するタグ
    companion object { private const val TAG = "FirebaseMemo" }

    // Viewが作成されるときの処理
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        // ViewBindingを用いてViewを生成
        binding = FragmentMainBinding.inflate(inflater, container, false)
        return binding.root
    }

    // Viewが作成された後の処理
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // RecyclerViewのLayoutManagerを設定
        binding.recyclerMemos.layoutManager = LinearLayoutManager(context)
        // FirestoreとRecyclerViewの初期設定を行うメソッドを呼び出し
        initFirestore()
        // "memos"コレクションのFirestoreクエリを作成
        query = firestore.collection("memos")
        // Firestoreからメモを取得し、成功した場合はアダプターを設定
        (query as CollectionReference)
            .get()
            .addOnSuccessListener {
                val document = it.documents
                adapter = createAdapter(document)
                binding.recyclerMemos.adapter = adapter
            }
            .addOnFailureListener { Toast.makeText(context,"Error!",Toast.LENGTH_SHORT).show() }
        // FAB（浮き出るアクションボタン）がクリックされたときに優先度ダイアログを表示するリスナーを設定
        binding.fabAddMemo.setOnClickListener { showMemoDialog() }
    }

    // Firestoreの初期設定を行うメソッド
    private fun initFirestore() {
        firestore = Firebase.firestore
        updateFireStoreQuery()
    }
    private fun updateFireStoreQuery() {
        query = firestore.collection("memos")
        registration = (query as CollectionReference)
            .addSnapshotListener { querySnapshot,e ->
                // エラーが発生したかのハンドリング
                if (e != null) { Toast.makeText(context,e.message,Toast.LENGTH_SHORT).show() }
                // データ更新の場合
                val documents = querySnapshot?.documents
                if (documents != null){
                    // 表示用のデータ更新
                    adapter = createAdapter(documents)
                    binding.recyclerMemos.adapter = adapter
                }
            }
    }
    // 新しいメモをFirestoreに追加するメソッド
    private fun add(memo: Memo):Task<Void> = firestore.collection("memos").document().set(memo)

    // エラー時にSnackbarでメッセージを表示するメソッド
    private fun showErrorSnackbar(message: String) { Snackbar.make(binding.root, "エラー: $message", Snackbar.LENGTH_LONG).show() }

    // メモダイアログを表示するメソッド
    private fun showMemoDialog(){
        val memoDialog = MemoDialogFragment()
        memoDialog.show(childFragmentManager, MemoDialogFragment.TAG)
    }

    // キーボードを隠すメソッド
    private fun hideKeyboard() {
        val view = requireActivity().currentFocus
        if (view != null) { (requireActivity().getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager).hideSoftInputFromWindow(view.windowToken, 0) }
    }
    // submitが選択されたときのコールバックメソッド
    override fun onCreateMemo(memo: Memo) {
    // メモのデータをFireStoreに追加する処理が必要
        add(memo)
            // if true
            .addOnSuccessListener { Toast.makeText(context,"OK!",Toast.LENGTH_SHORT).show() }
            // if false
             .addOnFailureListener { Toast.makeText(context,"Error!",Toast.LENGTH_SHORT).show() }
    }

    // メモの更新が行われた時の処理
    override fun onUpdateMemo(memo: Memo) {
        memo.documentId?.let {
            firestore.collection("memos")
                .document(it)
                .update("text",memo.text,"priority",memo.priority)
                .addOnSuccessListener { Toast.makeText(context,"更新に成功しました",Toast.LENGTH_SHORT).show() }
                .addOnFailureListener { Toast.makeText(context,"更新に失敗しました",Toast.LENGTH_SHORT).show() }
        }
    }

    // Firestoreのドキュメントからアダプターを作成するメソッド
    private  fun createAdapter(documents: List<DocumentSnapshot>): MemoAdapter {
        return MemoAdapter(documents){
            // メモ自信が押された時の処理を下記に記述
            // データの取得
            val memoData = it.toObject(Memo::class.java)?.copy(documentId = it.id)?:return@MemoAdapter
            // データをバンドルに設定
            val bundle = Bundle().apply { putSerializable("selectedMemo", memoData) }
            // 編集用のダイアログを表示
            val memoEditDialog = MemoEditDialogFragment().apply { arguments = bundle }
            memoEditDialog.show( childFragmentManager, MemoDialogFragment.TAG )
        }
    }
}


